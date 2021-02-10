import logging
import aiosqlite
from pathlib import Path

logger = logging.getLogger(__name__)


class DatabaseHandler:
    DB_NAME = "main.sqlite3"
    _connection = None

    @classmethod
    def get_connection(cls) -> aiosqlite.core.Connection:
        if cls._connection is None:
            raise ValueError("Global connection has to be created first!")
        return cls._connection

    @classmethod
    async def create_connection(cls) -> aiosqlite.core.Connection:
        if cls._connection is not None:
            return cls._connection
        else:
            return await cls._create_instance()

    @classmethod
    async def _create_instance(cls) -> aiosqlite.core.Connection:
        cls._connection = await cls._get_connection()
        logger.info("Connection to database established.")
        return cls._connection

    @classmethod
    async def _get_connection(cls) -> aiosqlite.core.Connection:
        """
        Returns a connection to the db, if db doesn't exist create new
        :return: aiosqlite.core.Connection
        """
        if Path(cls.DB_NAME).is_file():
            return await aiosqlite.connect(cls.DB_NAME)
        else:
            logger.info("Database not found! Creating fresh ...")
            return await DatabaseHandler._create_database(cls.DB_NAME)

    @staticmethod
    async def _create_database(path: str) -> aiosqlite.core.Connection:
        """
        :param path: path where database will be created, including file name and extension
        :return: aiosqlite.core.Connection
        """
        conn = await aiosqlite.connect(path)
        await conn.execute(
            """CREATE TABLE MEMBERS(
                USER_ID UNSIGNED BIG INT,
                GUILD_ID UNSIGNED BIG INT,
                COINS UNSIGNED INT DEFAULT 1,
                UNIQUE(USER_ID, GUILD_ID)
            )"""
        )

        await conn.commit()
        logger.info("Database successfully created!")
        return conn
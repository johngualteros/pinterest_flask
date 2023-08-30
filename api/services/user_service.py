from api.data import db_session
from api.data.users import User


def save_user(user) -> bool:
    try:
        user.validate()
        session = db_session.create_session()
        session.add(user)
        session.commit()
        session.close()
        return True
    except Exception as e:
        raise e


def get_all_users() -> list:
    session = db_session.create_session()
    users = session.query(User).all()
    session.close()
    return users

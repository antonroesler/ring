from streamlit.runtime.runtime import Runtime
from streamlit.runtime.scriptrunner import add_script_run_ctx
import hashlib

from ring.conf import settings
from ring.db.user import User, Users, Role

MAIL_HEADER = "X-Ms-Client-Principal-Name"


def _st_instance_of_type(type_obj: object) -> object:
    import gc

    st_obj = None
    for obj in gc.get_objects():
        if type(obj) is type_obj:
            st_obj = obj
            break
    return st_obj


def _st_session_info():
    st_runtime: Runtime = _st_instance_of_type(Runtime)
    # get session id from the current script runner thread
    session_id = add_script_run_ctx().streamlit_script_run_ctx.session_id
    # use the session id to retrieve the session info
    session_info = st_runtime._session_mgr.get_session_info(session_id)
    return session_info


def st_client_headers() -> dict:
    session_info = _st_session_info()
    client_headers = session_info.client.request.headers._dict
    return dict(client_headers)


def _get_mail_header():
    client_headers = st_client_headers()
    return client_headers.get(MAIL_HEADER, None)


def _get_user(uid) -> User | None:
    users = Users()
    return users.get(uid)


def hash_email(email: str) -> str:
    """Returns a hash of the email address."""
    return hashlib.md5(email.encode()).hexdigest()


def get_current_user() -> User:
    """Returns the current user."""
    if settings.local_mode:
        return User(username="local", role=Role.ADMIN, id=hash_email("local@local.com"))
    user_email = _get_mail_header()
    if user_email:
        return _get_user(hash_email(user_email))
    raise RuntimeError(f"Could not find header {MAIL_HEADER}")

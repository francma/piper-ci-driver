from typing import Dict
from typing import Any

from piper_driver.models import User
from piper_driver.repository.repository import Repository


class IdentityRepository(Repository):

    @staticmethod
    def get(idx, user: User) -> Dict[Any, Any]:
        result = {
            'id': user.id,
            'email': user.email,
            'role': user.role.to_str(),
            'token': user.token,
        }

        return result

    @staticmethod
    def update(idx, values: Dict[str, Any], user: User) -> None:
        allowed = {'email', 'token'}

        for k, v in values.items():
            if k in allowed:
                setattr(user, k, v)
        user.save()
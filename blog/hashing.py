from passlib.context import CryptContext


class Hash():
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def bcrypt(self, password):
        return self.pwd_context.hash(password)

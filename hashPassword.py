import bcrypt

def hash_password(password: str) -> str:
	password = str(password)[:72]  
	hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
	return hashed.decode('utf-8')
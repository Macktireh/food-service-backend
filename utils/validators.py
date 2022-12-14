import re
from typing import Any, Dict, Literal, Union


REGEX_EMAIL_VALIDATION = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
REGEX_PASSWORD_VALIDATION = r"\b^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$\b"
MESSAGE_PASSWORD_INVALID = "Password is invalid, Should be atleast 8 characters with upper and lower case letters, numbers and special characters"

def validate(regex: Literal, field: str) -> bool:
    """Custom Validator"""
    return True if re.match(regex, field) else False

def validate_password(password: str) -> bool:
    """Password Validator"""
    return validate(REGEX_PASSWORD_VALIDATION, password)

def validate_email(email: str) -> bool:
    """Email Validator"""
    return validate(REGEX_EMAIL_VALIDATION, email)

# def validate_book(**args):
#     """Book Validator"""
#     if not args.get('title') or not args.get('image_url') \
#         or not args.get('category') or not args.get('user_id'):
#         return {
#             'title': 'Title is required',
#             'image_url': 'Image URL is required',
#             'category': 'Category is required',
#             'user_id': 'User ID is required'
#         }
#     if args.get('category') not in ['romance', 'peotry', 'politics' 'picture book', 'science', 'fantasy', 'horror', 'thriller']:
#         return {
#             'status': 'error',
#             'message': 'Invalid category'
#         }
#     try:
#         ObjectId(args.get('user_id'))
#     except:
#         return {
#             'user_id': 'User ID must be valid'
#         }
#     if not isinstance(args.get('title'), str) or not isinstance(args.get('description'), str) \
#         or not isinstance(args.get('image_url'), str):
#         return {
#             'title': 'Title must be a string',
#             'description': 'Description must be a string',
#             'image_url': 'Image URL must be a string'
#         }
#     return True

def validate_user(**args: Dict[str, Any]) -> Union[Dict[str, str], Literal[True]]:
    """User Validator"""
    if  not args.get('email') or not args.get('password') or not args.get('firstName') or not args.get('lastName'):
        return {
            'email': 'Email is required',
            'firstName': 'firstName is required',
            'lastName': 'lastName is required',
            'password': 'Password is required',
        }
    if not isinstance(args.get('email'), str) or not isinstance(args.get('password'), str):
        return {
            'email': 'Email must be a string',
            'firstName': 'firstName must be a string',
            'lastName': 'lastName must be a string',
            'password': 'Password must be a string',
        }
    if not validate_email(args.get('email')):
        return {
            'email': 'Email is invalid'
        }
    if not validate_password(args.get('password')):
        return {
            'password': MESSAGE_PASSWORD_INVALID
        }
    # if not 2 <= len(args['firstName'].split(' ')) <= 10:
    #     return {
    #         'firstName': 'firstName must be between 2 and 10 words'
    #     }
    # if not 2 <= len(args['lastName'].split(' ')) <= 10:
    #     return {
    #         'lastName': 'lastName must be between 2 and 10 words'
    #     }
    return True

def validate_email_and_password(email: str, password: str) -> Union[Dict[str, str], Literal[True]]:
    """Email and Password Validator"""
    if not (email and password):
        return {
            'email': 'Email is required',
            'password': 'Password is required'
        }
    # if not validate_email(email):
    #     return {
    #         'email': 'Email is invalid'
    #     }
    # if not validate_password(password):
    #     return {
    #         'password': 'Password is invalid, Should be atleast 8 characters with upper and lower case letters, numbers and special characters'
    #     }
    return True

def check_password_and_passwordConfirm(password: str, passwordConfirm: str) -> bool:
    """Validate the match between the password and the passwordConfirm"""
    return password == passwordConfirm
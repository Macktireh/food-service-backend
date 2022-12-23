from typing import Optional, TypedDict


class ProductType(TypedDict): 
    name: str 
    categoryId: Optional[int]
    price: float
    description: Optional[str]
    image: Optional[str]
    available: Optional[bool]
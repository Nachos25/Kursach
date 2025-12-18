# Domain Entities — Perforator / Ябко+ Tech Store

## Піддомени та ключові сутності

### 1. Catalog (Каталог)
- **Product**  
  - id: int  
  - name: str  
  - description: str  
  - price: float  
  - discount: float  
  - category: Category  
  - brand: Brand  
  - image_url: str  
  - Methods: get_price_after_discount()

- **Category**  
  - id: int  
  - name: str

- **Brand**  
  - id: int  
  - name: str

### 2. Users (Користувачі)
- **User**  
  - id: int  
  - username: str  
  - email: str  
  - password_hash: str  
  - Methods: check_password(password)

### 3. Orders (Замовлення)
- **Order**  
  - id: int  
  - user: User  
  - items: List[OrderItem]  
  - status: str (OPEN, COMPLETED)  
  - Methods: add_item(product, quantity), total_amount()

- **OrderItem**  
  - product: Product  
  - quantity: int  
  - Methods: subtotal()

### 4. Payments (Оплати) — майбутнє
- **Payment**  
  - id: int  
  - order: Order  
  - amount: float  
  - status: str (PENDING, PAID, FAILED)  
  - Methods: process()

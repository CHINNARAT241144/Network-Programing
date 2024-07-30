import asyncio

async def main():
    print('CHINNARAT')
    task = asyncio.create_task(foo('text')) # สร้าง task และส่งค่า text ไปให้ foo   
    print('finish')

async def foo(text):
    print(text)
    await asyncio.sleep(5000)
    
asyncio.run(main())

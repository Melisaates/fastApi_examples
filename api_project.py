from tokenize import String
from fastapi import FastAPI,Body



product = {
	"id": 218,
	"product_name": "Margarita",
	"short_description": "Pizza Sosu Mozzarella Peyniri",
	"description": "",
	"product_code": "MRGT02",
	"tags": [],
	"make_time": 15,
	"calorie": 100,
	"price": [
		{
			"id": 110,
			"price": 37.99,
			"is_default": False,
			"order_delivery_type_id": "TABLE"
		}
	],
	"images": [
		{
			"id": 804,
			"image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-daily-menu-ph-margherita-big-0-6479394777655054.jpeg",
			"list_order": 1910,
			"image_size_id": "mobile_daily_menu"
		},
		{
			"id": 805,
			"image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-list-ph-margherita-big-0-4629594528048909.jpeg",
			"list_order": 1910,
			"image_size_id": "mobile_list"
		},
		{
			"id": 806,
			"image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-list-col-ph-margherita-big-0-9935630810104057.jpeg",
			"list_order": 1910,
			"image_size_id": "mobile_list_col"
		},
		{
			"id": 807,
			"image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-detail-ph-margherita-big-0-19859779590268745.jpeg",
			"list_order": 1910,
			"image_size_id": "mobile_detail"
		}
	],
	"option_groups": [
		{
			"id": 56,
			"options": [
				{
					"id": 163,
					"is_free": True,
					"add_price": 0,
					"is_default": False,
					"list_order": 1,
					"option_code": "",
					"option_name": "pizza sosu"
				}
			],
			"max_count": 0,
			"list_order": 1,
			"description": "",
			"adding_type_id": "DECREASE",
			"choose_type_id": "MULTIPLE",
			"option_group_name": "Çıkarılacak Malzemeler"
		},
		{
			"id": 57,
			"options": [
				{
					"id": 164,
					"is_free": False,
					"add_price": 10.2,
					"is_default": True,
					"list_order": 1,
					"option_code": "",
					"option_name": "İncecik Hamur"
				},
				{
					"id": 165,
					"is_free": False,
					"add_price": 3.0,
					"is_default": False,
					"list_order": 2,
					"option_code": "",
					"option_name": "Klasik Hamur"
				}
			],
			"max_count": 0,
			"list_order": 2,
			"description": "",
			"adding_type_id": "ADD",
			"choose_type_id": "SINGLE",
			"option_group_name": "Hamur Seçimi"
		}
	],
	"features": None
}
app = FastAPI()


"""@app.post("/products/{product_id}")
async def create_product(product_id:int):
    return product[product_id]"""


@app.get("/products/{product_id}")
async def read_item(product_id: int):
	product_id = product.get("id")
	return product_id

@app.post("/products/")
async def create_product(color:str=Body(...,embed=True)):
	color={"color":"black"}
	return product

@app.put("/product/")
async def update_product(product_id:int=Body(...,embed=True)):
	print(product_id)
	product.update({"id":product_id})
	return product

@app.delete("/product")
async def product_deleting(product_key:str):
	
	product_key="id"
	del product[product_key]
	return product


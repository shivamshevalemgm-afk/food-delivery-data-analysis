import pandas as pd
import random
import os

random.seed(42)

restaurants = pd.read_csv("data/restaurants.csv")

OUTPUT_FILE = "data/menu_items.csv"

os.makedirs("data", exist_ok=True)

categories = [
    "Starter",
    "Main Course",
    "Snack",
    "Dessert",
    "Beverage"
]

menu = {

"North Indian":[
("Butter Chicken","Main Course","No"),
("Paneer Butter Masala","Main Course","Yes"),
("Dal Makhani","Main Course","Yes"),
("Naan","Main Course","Yes"),
("Tandoori Roti","Main Course","Yes"),
("Chicken Tikka","Starter","No"),
("Paneer Tikka","Starter","Yes"),
("Gulab Jamun","Dessert","Yes"),
("Lassi","Beverage","Yes"),
("Jeera Rice","Main Course","Yes")
],

"South Indian":[
("Masala Dosa","Main Course","Yes"),
("Plain Dosa","Main Course","Yes"),
("Idli","Main Course","Yes"),
("Medu Vada","Snack","Yes"),
("Uttapam","Main Course","Yes"),
("Filter Coffee","Beverage","Yes"),
("Curd Rice","Main Course","Yes"),
("Pongal","Main Course","Yes"),
("Kesari","Dessert","Yes"),
("Sambar Rice","Main Course","Yes")
],

"Chinese":[
("Hakka Noodles","Main Course","Yes"),
("Chicken Noodles","Main Course","No"),
("Veg Fried Rice","Main Course","Yes"),
("Chicken Fried Rice","Main Course","No"),
("Manchurian","Starter","Yes"),
("Spring Roll","Starter","Yes"),
("Momos","Snack","No"),
("Chilli Paneer","Starter","Yes"),
("Hot Soup","Starter","Yes"),
("Cold Drink","Beverage","Yes")
],

"Italian":[
("Margherita Pizza","Main Course","Yes"),
("Farmhouse Pizza","Main Course","Yes"),
("Pepperoni Pizza","Main Course","No"),
("White Sauce Pasta","Main Course","Yes"),
("Red Sauce Pasta","Main Course","Yes"),
("Garlic Bread","Snack","Yes"),
("Tiramisu","Dessert","Yes"),
("Cold Coffee","Beverage","Yes"),
("Cheese Pizza","Main Course","Yes"),
("Veg Lasagna","Main Course","Yes")
],

"Fast Food":[
("Veg Burger","Main Course","Yes"),
("Chicken Burger","Main Course","No"),
("French Fries","Snack","Yes"),
("Pizza Puff","Snack","Yes"),
("Sandwich","Snack","Yes"),
("Cold Drink","Beverage","Yes"),
("Milkshake","Beverage","Yes"),
("Brownie","Dessert","Yes"),
("Wrap","Main Course","No"),
("Hot Dog","Main Course","No")
]
}

default_items=[
("Veg Meal","Main Course","Yes"),
("Chicken Meal","Main Course","No"),
("Paneer Roll","Snack","Yes"),
("French Fries","Snack","Yes"),
("Cold Coffee","Beverage","Yes"),
("Ice Cream","Dessert","Yes"),
("Soup","Starter","Yes"),
("Brownie","Dessert","Yes"),
("Tea","Beverage","Yes"),
("Coffee","Beverage","Yes")
]

rows=[]
menu_item_id=1

for _,restaurant in restaurants.iterrows():

    cuisine=restaurant["cuisine"]

    items=menu.get(cuisine,default_items)

    for i in range(20):

        item=random.choice(items)

        rows.append({

            "menu_item_id":menu_item_id,

            "restaurant_id":restaurant["restaurant_id"],

            "item_name":item[0],

            "category":item[1],

            "cuisine":cuisine,

            "is_veg":item[2],

            "price":random.randint(79,999),

            "preparation_time_min":random.randint(5,45),

            "calories":random.randint(100,1200),

            "is_available":random.choice(["Yes","Yes","Yes","No"])

        })

        menu_item_id+=1

menu_df=pd.DataFrame(rows)

menu_df.to_csv(OUTPUT_FILE,index=False)

print("✅ menu_items.csv generated successfully!")
print("Rows:",len(menu_df))
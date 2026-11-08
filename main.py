import pandas as pd
import matplotlib.pyplot as plt

data = {
    'نام محصول': ['گوشی موبایل', 'هدفون', 'شارژر', 'اسپیکر', 'پاوربانک'],
    'شناسه محصول': [101, 102, 103, 104, 105],
    'دسته بندی محصول': ['الکترونیکی', 'صوتی', 'لوازم جانبی', 'صوتی', 'لوازم جانبی'],
    'قیمت تمام شده': [8000000, 500000, 200000, 900000, 1200000],
    'قیمت فروش': [10000000, 700000, 300000, 1200000, 1500000],
    'درصد تخفیف': [10, 5, 0, 10, 5],
    'تعداد فروش': [20, 30, 15, 10, 25],
    'تاریخ فروش': ['1405/07/05', '1405/07/10', '1405/07/15', '1405/07/20', '1405/07/25'],
    'شهر فروش': ['اصفهان', 'تهران', 'شیراز', 'اصفهان', 'تبریز']
}

df = pd.DataFrame(data)

df['مجموع فروش'] = df['قیمت فروش'] * (1 - df['درصد تخفیف'] / 100) * df['تعداد فروش']

print(df)

total_sales = df['مجموع فروش'].sum()
print("مجموع فروش ماه:", total_sales)

product_sales = df.groupby('نام محصول')['مجموع فروش'].sum()
print("مجموع فروش هر محصول:")
print(product_sales)

best_product = df.loc[df['تعداد فروش'].idxmax()]
print("پر فروش ترین محصول:", best_product['نام محصول'])

worst_product = df.loc[df['تعداد فروش'].idxmin()]
print("کم فروش ترین محصول:", worst_product['نام محصول'])

plt.bar(df['نام محصول'], df['تعداد فروش'])
plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Number of Sales")
plt.show()

plt.pie(
    df['تعداد فروش'],
    labels=df['نام محصول'],
    autopct="%1.1f%%"
)
plt.title("Product Sales Percentage")
plt.show()

df['ماه'] = df['تاریخ فروش'].str.split('/').str[1]

daily_sales = df.groupby('تاریخ فروش')['مجموع فروش'].sum()

monthly_average = daily_sales.groupby(
    df.groupby('تاریخ فروش')['ماه'].first()
).mean()

plt.plot(monthly_average.index, monthly_average.values, marker="o")
plt.title("Monthly Average Sales")
plt.xlabel("Month")
plt.ylabel("Average Sales")
plt.grid(True)
plt.show()
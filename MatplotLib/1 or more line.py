import matplotlib.pyplot as plt

# line 1 এর পয়েন্ট
x1 = [10, 20, 30]
y1 = [20, 40, 10]

# line 2 এর পয়েন্ট
x2 = [10, 20, 30]
y2 = [40, 10, 30]

# লেবেল ও টাইটেল
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Plot with two or more lines with different styles')

# line 1 প্লট
plt.plot(x1, y1, color='blue', linewidth=3, label='line1-dotted', linestyle='dotted')

# line 2 প্লট
plt.plot(x2, y2, color='red', linewidth=5, label='line2-dashed', linestyle='dashed')

# legend দেখানো
plt.legend()

# গ্রাফ দেখানো
plt.show()
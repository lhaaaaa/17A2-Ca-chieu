"""
Viết chương trình yêu cầu người dùng nhập vào tọa độ của bốn đỉnh M, N, P,
Q của một tứ giác. Chương trình sẽ tính toán và in ra tọa độ trung điểm của
mỗi cạnh của tứ giác.
"""
# Nhập tọa độ đỉnh M
xm, ym = map(float, input("Nhập tọa độ của đỉnh M: ").split())

# Nhập tọa độ đỉnh N
xn, yn = map(float, input("Nhập tọa độ của đỉnh N: ").split())

# Nhập tọa độ đỉnh P
xp, yp = map(float, input("Nhập tọa độ của đỉnh P: ").split())

# Nhập tọa độ đỉnh Q
xq, yq = map(float, input("Nhập tọa độ của đỉnh Q: ").split())

# Tính tọa độ trung điểm của MN
xmn = (xm + xn)/2
ymn = (ym + yn)/2

# Tính tọa độ trung điểm của NP
xnp = (xp + xn)/2
ynp = (yp + yn)/2

# Tính tọa độ trung điểm của PQ
xpq = (xp + xq)/2
ypq = (yp + yq)/2

# Tính tọa độ trung điểm của QM
xqm = (xm + xq)/2
yqm = (ym + yq)/2

# In ra tọa độ trung điểm
print(
"""
Tọa độ trung điểm của cạnh MN là: ({},{})
Tọa độ trung điểm của cạnh NP là: ({},{})
Tọa độ trung điểm của cạnh PQ là: ({},{})
Tọa độ trung điểm của cạnh QM là: ({},{})
""".format(xmn,ymn,xnp,ynp,xpq,ypq,xqm,yqm)
)


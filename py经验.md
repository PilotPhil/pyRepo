## 1. scipy中的weibull 及 其累计分布函数的逆函数

```python
import scipy as sp
cd=sp.stats.exponweib.cdf(x,n,k)
iss=sp.stats.exponweib.ppf(x,n,k) # 百分位函数（累计分布函数的逆函数）
```

## 2. 空数组

```python
used=np.asarray([],dtype=int)  # 被使用过的点
```

## 3. 禁用警告

```python
import warnings
warnings.filterwarnings("ignore")
```

## 4. 开n次方根

```python
pow(a, 1/n)
```

## 5.梯形法积分  [trapz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.trapz.html?highlight=trapz#scipy.integrate.trapz)

```python
scipy.integrate.trapz(y, x=None, dx=1.0, axis=- 1)
```

## 6.matplotlib在图像中添加文字

```python
import matplotlib.pyplot as plt

plt.plot([0, 2], [0, 2])
plt.text(0.5, 1, 'put some text')
plt.show()
```

## 7.
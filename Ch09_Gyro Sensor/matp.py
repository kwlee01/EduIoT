#https://datascienceschool.net/view-notebook/d0b1637803754bb083b5722c9f2209d0/
#<matplotlib install>
#$ sudo apt-get install python-pip
#$ sudo apt-get install python-matplotlib
import numpy as np   # if necessary
#%================== 라인 플롯
import matplotlib as mpl
import matplotlib.pylab as plt
plt.title("Plot")
plt.plot([1, 4, 9, 16])
plt.show()

#%============== x tick 명시
#plt.title("x축의 tick 위치를 명시")
plt.title("tick of x-axis")
plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
plt.show()

#%================ 스타일 지정
#plt.title("'rs--' 스타일의 plot ")
plt.title("'rs--' style plot")
plt.plot([10, 20, 30, 40], [1, 4, 9, 16], 'rs--')
plt.show()

#%========== 색깔
#blue b
#green g
#red r
#cyan c
#magenta m
#yellow y
#black k
#white w

#%========= 마커
#. point marker
#, pixel marker
#o circle marker
#v triangle_down marker
#^ triangle_up marker
#< triangle_left marker
#> triangle_right marker
#1 tri_down marker
#2 tri_up marker
#3 tri_left marker
#4 tri_right marker
#s square marker
#p pentagon marker
#* star marker
#h hexagon1 marker
#H hexagon2 marker
#+ plus marker
#x x marker
#D diamond marker
#d thin_diamond marker

#%======= 선 스타일
#- solid line style
#-- dashed line style
#-. dash-dot line style
#: dotted line style

#%========= 기타 스타일
#color c 선 색깔
#linewidth lw 선 굵기
#linestyle ls 선 스타일
#marker  마커 종류
#markersize ms 마커 크기
#markeredgecolor mec 마커 선 색깔
#markeredgewidth mew 마커 선 굵기
#markerfacecolor mfc 마커 내부 색깔

#%=====================
plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c="b",
         lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
#plt.title("스타일 적용 예")
plt.title("Style example ")
plt.show()

#%====================== 그림 범위 지정
#plt.title("x축, y축의 범위 설정")
plt.title("limit of x, y axis")
plt.plot([10, 20, 30, 40], [1, 4, 9, 16],
         c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
plt.xlim(0, 50)
plt.ylim(-10, 30)
plt.show()

#%====================== 틱(tick) 설정
X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
#plt.title("x축과 y축의 tick label 설정")
plt.title("Setting of limit of x, y axis")
plt.plot(X, C)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
plt.yticks([-1, 0, +1])
plt.show()

#%======================
X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
#plt.title("LaTeX, 문자열로 tick label 정의")
plt.title("Latex, define tick label with string")
plt.plot(X, C)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           ['$-\pi$', '$-\pi/2$', '$0$', '$+\pi/2$', '$+\pi$'])
plt.yticks([-1, 0, 1], ["Low", "Zero", "High"])
plt.show()

#%=================== 그리드 설정
X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
#plt.title("Grid 제거")
plt.title("Removed Grid")
plt.plot(X, C)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, 1], ["Low", "Zero", "High"])
plt.grid(False)
plt.show()

#%========== 여러개 선 그리기
t = np.arange(0., 5., 0.2)
#plt.title("라인 플롯에서 여러개의 선 그리기")
plt.title("Multiple line in line plot")
plt.plot(t, t, 'r--', t, 0.5 * t**2, 'bs:', t, 0.2 * t**3, 'g^-')
plt.show()

#%==== 홀드 명령
#plt.title("복수의 plot 명령을 한 그림에서 표현")
plt.title("Multiple plot in a figure")
plt.plot([1, 4, 9, 16],
         c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
# plt.hold(True)   # <- 1,5 버전에서는 이 코드가 필요하다.
plt.plot([9, 16, 4, 1],
         c="k", lw=3, ls=":", marker="s", ms=10, mec="m", mew=5, mfc="c")
# plt.hold(False)  # <- 1,5 버전에서는 이 코드가 필요하다.
plt.show()

#%============== 범례
#best 0
#upper right 1
#upper left 2
#lower left 3
#lower right 4
#right 5
#center left 6
#center right 7
#lower center 8
#upper center 9
#center 10

#%================= 축 라벨, 타이틀
X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C, label="cosine")
plt.plot(X, S, label="sine")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("Cosine & Sine  Plot")
plt.grid(True)
plt.legend(loc=2)
plt.show()

#%================= Figure 객체
np.random.seed(0)
f1 = plt.figure(figsize=(10, 2))
plt.title("figure size : (10, 2)")
plt.plot(np.random.randn(100)) # mean:0, standard dev:1
plt.show()

print('================= Axes 객채와 subplot명령')
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

ax1 = plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'yo-')
plt.title('Pots of 2 subplots')
plt.ylabel('Damped oscillation')
print(ax1)

ax2 = plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')
print(ax2)

plt.tight_layout()
plt.show()

print('%=================')
np.random.seed(0)

plt.subplot(221)
plt.plot(np.random.rand(5))
plt.title("axes 1")

plt.subplot(222)
plt.plot(np.random.rand(5))
plt.title("axes 2")

plt.subplot(223)
plt.plot(np.random.rand(5))
plt.title("axes 3")

plt.subplot(224)
plt.plot(np.random.rand(5))
plt.title("axes 4")

plt.tight_layout()
plt.show()

print('%==============')
fig, axes = plt.subplots(2, 2)

np.random.seed(0)
axes[0, 0].plot(np.random.rand(5))
axes[0, 0].set_title("axes 1")
axes[0, 1].plot(np.random.rand(5))
axes[0, 1].set_title("axes 2")
axes[1, 0].plot(np.random.rand(5))
axes[1, 0].set_title("axes 3")
axes[1, 1].plot(np.random.rand(5))
axes[1, 1].set_title("axes 4")

plt.tight_layout()
plt.show()

print('=============== Axis 객체와 축 ===')

fig, ax0 = plt.subplots()
ax1 = ax0.twinx()
#ax0.set_title("2개의 y축 한 figure에서 사용하기")
ax0.set_title("Using 2 y-axis in a figure")
In1=ax0.plot([10, 5, 2, 9, 7], 'r-', label="y0")
ax0.set_ylabel("y0")
#plt.legend(loc=1)
ax0.grid(False)
In2=ax1.plot([100, 200, 220, 180, 120], 'g:', label="y1")
ax1.set_ylabel("y1")
ax1.grid(False)
#ax0.set_xlabel("공유되는 x축")
ax0.set_xlabel("Shared x-axis")
#plt.legend(loc=2)
ax0.legend(loc=2)
#ax1.legend()
Ins = In1 + In2
labs =[l.get_label() for l in Ins]
ax0.legend(Ins, labs, loc=0)
plt.show()


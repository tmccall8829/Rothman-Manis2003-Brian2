import matplotlib.pyplot as plt

brian1_times = [1.96640300751, 1.95334386826, 2.03092598915, 3.95970106125,
                6.70688605309, 11.1532299519, 15.8273820877, 20.5792498589]
brian2_times = [3.22265195847, 2.85981893539, 2.90201401711, 3.70192503929,
                4.7930700779, 6.86188602448, 8.79096603394, 10.8173658848]
cells        = [1, 10, 100, 1000, 2500, 5000, 7500, 10000]

plt.plot(cells, brian1_times, "-o", label="Brian1")
plt.plot(cells, brian2_times, "-o", label="Brian2")
plt.xlabel("# cells")
plt.ylabel("Time (s)")
plt.title("Rothman & Manis 2003 model using Brian versions 1 & 2")
plt.legend()
plt.savefig("Rothman_Manis_2003-Brian_tests.png")

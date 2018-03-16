import matplotlib.pyplot as plt, mpld3

fig = plt.figure()
plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
mpld3.show()
mpld3.save_html(fig,fileobj="testMpld3.html",no_extras=True,template_type="general")

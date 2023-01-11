#%%
import datetime

#%%
birthday = datetime.date(1991, 4, 1)

#%%
type(birthday)

# %%
birthday.strftime("I was born on a %A in the month of %B")

# %%
datetime.date.today()

# %%
datetime.datetime.now()
# %%
date_today = datetime.date.today()
# %%
date_today.strftime("%B")

# %% Subtracting the dates results in timedelta
birthday - date_today

# %% use timedelta 
date_today - datetime.timedelta(weeks=40)

# %%

is_raining=True
have_umbrella=False

if is_raining and have_umbrella:
    print("It is raining, but you have an umbrella. You can go outside!")
elif is_raining and not have_umbrella:
    print("It is raining and you don't have an umbrella. Better stay inside!")
else:
    print("It is not raining. You can go outside freely.")
from gacha_rate import capsule_toy

capsule = capsule_toy()
num = capsule.select()
choice = capsule.choice(num)
show = capsule.show(choice)

for commandment in Commandments.objects.all():
if not commandment.social:
	commandment.social = False
if not commandment.faith:
	commandment.faith = False
if not commandment.ritual:
	commandment.ritual = False
if not commandment.monetary:
	commandment.monetary = False
if not commandment.speech:
	commandment.speech = False
if not commandment.holidays:
	commandment.holidays = False
if not commandment.food:
	commandment.food = False
if not commandment.criminal:
	commandment.criminal = False
if not commandment.intimacy:
	commandment.intimacy = False
if not commandment.idolatry:
	commandment.idolatry = False
commandment.save()

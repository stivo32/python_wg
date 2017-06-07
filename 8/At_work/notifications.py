from datetime import date


class Notification(object):
	slug = None
	title = None
	body = None

	def __init__(self, **params):
		self.params = params

	def render(self):
		context = self.get_render_context()
		context.update(self.params)
		return '{}\n{}\n\n'.format(self.title, self.body).format(**context)

	def get_render_context(self):
		return {}


class DateTodayContextMixin(object):
	def get_render_context(self):
		context = super(DateTodayContextMixin, self).get_render_context()
		context.update({
			'date_today': date.today().isoformat(),
		})


class NotificationManager(object):
	notifications = {}

	@classmethod
	def register(cls, notification_cls):
		if not issubclass(notification_cls, Notification):
			raise RuntimeError('Not a Notification!')

		slug = notification_cls.slug
		cls.notifications[slug] = notification_cls
		return notification_cls

	@classmethod
	def send(cls, notification_slug, recipients, **params):
		notification_cls = cls.notifications.get(notification_slug)
		if not notification_cls:
			raise Exception()

		notification = notification_cls(**params)
		for recipient in recipients:
			print '{} -> {}'.format(
					recipient,
					notification.render())


@NotificationManager.register
class NewTankNotification(DateTodayContextMixin, Notification):
	slug = 'new_tank'
	title = 'New tank released, {date_today}'
	body = 'Tank_name:{tank_name}'


@NotificationManager.register
class InviteToClanNotification(DateTodayContextMixin, Notification):
	slug = 'invite_to_clan'
	title = 'You have been invited to clan "{clan_name}"'
	body = '...'

NotificationManager.send(
		'new_tank',
        ['Alex', 'Petya'],
		tank_name='KV2'
)

NotificationManager.send(
		'invite_to_clan',
        ['Kirill'],
		clan_name='WG'
)

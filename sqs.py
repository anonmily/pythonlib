import boto3

sqs = boto3.client('sqs')

class Queue():
	def __init__(self, QUEUE_URL):
		self.url = QUEUE_URL
	def send(self, message):
		''' Response:
			{
				'MD5OfMessageBody': 'fb1083d318e350b368e3369f92578781', 
				'ResponseMetadata': {
					'HTTPStatusCode': 200, 
					'RequestId': '7f817e4c-8759-55d1-95fc-3191a0e88458'
				}, 
				'MessageId': 'fb14b0a3-e6b2-4978-9098-4c6b37b3bdfc'
			}
		'''
		return sqs.send_message(
			QueueUrl=self.url,
			MessageBody=str(message)
		)

	def get(self):
		'''
		{'Messages': 
			[
				{
					'Body': 'http://www.discounttiredirect.com/direct/filterWheelProducts.do?pgWheels=0&vid=008845&yr=1961&wd=16&wth=7&rw=&bp=&counter=5&fl=&sortBy=prca&fqs=true', 
					'ReceiptHandle': 'AQEBrG6H5hA3jnjLWctEAoxMWvgD0C0LScjg4xgjhHQwgOzczQC0zrQzUUFRhBQKjuuesAZbYpvFJwAQ/JQezv+erpNhlZ+swfDlGxi1qwsjz7s1ovVammvkyTn9pxLGeODpAVlZw/0jfnNvBplnC6+gHzMAgs6eyuCH0g0IVuezJ6DQUwCuAUyM03Gw9TmsoBz3rFTYry/VuYVAENJRaBJP3gBUuVZFl7Nvvlx56XuOn86SfwBqzIMZ5+UlRBoURwlh42hgFS/uEVQBbFS5rePXOlzBqUYos5YcSSksSum2eyp2jBaKjWzfwOJDZFeYVHmx5meVVQEidNkwhHw3vVTTQnIQZ651bVFTR2tu6JcOT9Xf9TjFFOFup9xFtRceVbT37mHRvMFOrB8kWiPhBg2Jow==', 
					'MD5OfBody': 'fb1083d318e350b368e3369f92578781', 
					'MessageId': 'a15d68c9-f4a6-4ece-8df4-5130c7decdd0'
				}
			], 
			ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '6b2efb5e-71b9-5c66-89f4-b483576ca147'}
		}
		'''
		message = sqs.receive_message( QueueUrl=self.url )

		if 'Messages' in message:
			sqs_message = message['Messages'][0]
			return QueueMessage( sqs_message )
		else:
			return False

	def dequeue(self, receipt_handle):
		return sqs.delete_message(
			QueueUrl= self.url,
			ReceiptHandle=receipt_handle
		)

class QueueMessage:
	def __init__(self, sqs_message):
		self.body = sqs_message['Body']
		self.receipt_handle = sqs_message['ReceiptHandle']
		self.md5_body = sqs_message['MD5OfBody']
		self.message_id = sqs_message['MessageId']
	def remove(self):
		dequeue(self.receipt_handle)

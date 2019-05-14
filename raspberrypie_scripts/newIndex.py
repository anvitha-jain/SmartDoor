import boto3
import json

session = boto3.Session(aws_access_key_id='', aws_secret_access_key='', region_name='us-east-1')

bucket="test-reko-mybucket"
key="p1.jpg"
customName = "poorva"

bucket='test-reko-mybucket'
collectionId='friends_collection'
photo='nk4.jpg'
photoName = 'NightKing'

reko_client=session.client('rekognition')

response=reko_client.index_faces(CollectionId=collectionId,
							Image={'S3Object':{'Bucket':bucket,'Name':photo}},
							ExternalImageId=photoName,
							MaxFaces=1,
							QualityFilter="AUTO",
							DetectionAttributes=['ALL'])

print ('Results for ' + photo) 	
print('Faces indexed:')						
for faceRecord in response['FaceRecords']:
	 print('  Face ID: ' + faceRecord['Face']['FaceId'])
	 print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

print('Faces not indexed:')
for unindexedFace in response['UnindexedFaces']:
	print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
	print(' Reasons:')
	for reason in unindexedFace['Reasons']:
		print('   ' + reason)


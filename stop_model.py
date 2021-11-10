
import boto3
import time


def stop_model(model_arn):

    client=boto3.client('rekognition')

    print('Stopping model:' + model_arn)

    #Stop the model
    try:
        response=client.stop_project_version(ProjectVersionArn=model_arn)
        status=response['Status']
        print ('Status: ' + status)
    except Exception as e:  
        print(e)  

    print('Done...')
    
def main():
    
    model_arn='arn:aws:rekognition:eu-west-1:445264091443:project/Natural_lightHD/version/Natural_lightHD.2021-11-09T23.54.15/1636498455677'
    stop_model(model_arn)

if __name__ == "__main__":
    main() 
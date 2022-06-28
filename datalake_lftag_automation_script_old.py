from traceback import print_tb
import boto3

AWS_REGION = "us-east-1"
tag_key = "temp"
tag_val = ['temp1', 'temp2']

def createLFTags():
    client = boto3.client('lakeformation', region_name=AWS_REGION)
    response = client.create_lf_tag(
        TagKey=tag_key,
        TagValues=[
            tag_val
        ]
    )
    
def updateLFtag():
    client = boto3.client('lakeformation', region_name=AWS_REGION)
    response = client.update_lf_tag(
        TagKey=tag_key,
        TagValuesToAdd=tag_val
    )

def ListLFTag():
    client = boto3.client('lakeformation', region_name=AWS_REGION)
    response = client.list_lf_tags(
        ResourceShareType='ALL',
        MaxResults=123
    )

    is_tag_key_unique = True
    is_tag_val_unique = True

    for i in response["LFTags"]:
        if tag_key == i['TagKey']:
            is_tag_key_unique = False
            if tag_val == i['TagValue']:
                is_tag_val_unique = False

    if is_tag_key_unique == False & is_tag_val_unique == True:
        print('Warning')
    elif is_tag_val_unique == False:
        updateLFtag()
    else:
        createLFTags()


if __name__ == "__main__":
    ListLFTag()

import boto3

AWS_REGION = "us-east-1"
TAG_KEY = "a1"
TAG_VAL = ['a1', 'a2', 'a3']


def createLFTags(client):
    print('create :::')
    try:
        response = client.create_lf_tag(
            TagKey=TAG_KEY,
            TagValues=TAG_VAL
        )
    except Exception as e:
        print(e)


def UPDTAE_LFTAG(client):
    print('update :::')
    try:
        response = client.update_lf_tag(
            TagKey=TAG_KEY,
            TagValuesToAdd=TAG_VAL
        )
    except Exception as e:
        print(e)


def ListLFTag(client):
    try:
        response = client.list_lf_tags(
            ResourceShareType='ALL',
            MaxResults=123
        )
    except Exception as e:
        print(e)
    data = {}
    try:
        for i in response["LFTags"]:
            data[i["TagKey"]] = i["TagValues"]
    except Exception as e:
        print(e)
    isTAGKEYUnique = True
    isTagValuenique = True
    try:
        for key, value in data.items():
            if TAG_KEY == key:  # c
                isTAGKEYUnique = False
                if TAG_VAL == value:
                    isTagValuenique = False
    except Exception as e:
        print(e)
    try:
        if isTAGKEYUnique == False and isTagValuenique == True:
            UPDTAE_LFTAG(client)
        elif isTAGKEYUnique == False and isTagValuenique == False:
            print('Both are Exsisted')
        else:
            createLFTags(client)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    client = boto3.client('lakeformation', region_name=AWS_REGION)
    ListLFTag(client)

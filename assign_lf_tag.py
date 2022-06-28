import json

import boto3


def assign_lf_tag():
    client = boto3.client('lakeformation', region_name=AWS_REGION)
    for key, value in data.items():
        try:
            client.add_lf_tags_to_resource(
                Resource={
                    'Database': {
                        'Name': key.format(ENV, PIPELINE_NAME)
                    },
                },
                LFTags=[
                    {
                        'TagKey': value['LFTagKey'],
                        'TagValues': value['LFTagValues']
                    },
                ]
            )
            print(
                f"Successfully assign {value['LFTagKey']} Tag Key and {value['LFTagValues']} Tag Value to {key.format(ENV, PIPELINE_NAME)} database")
        except Exception as exception:
            print(f'Exception : {exception}')


if __name__ == "__main__":
    AWS_REGION = "us-east-1"
    ENV = "dev"
    PIPELINE_NAME = "dataengg"
    f = open('json_data.json', encoding="utf-8")
    data = json.load(f)
    print(data)
    f.close()
    assign_lf_tag()

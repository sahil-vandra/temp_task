# new content file 
AWS_REGION = "us-east-1"
ENV = "dev"
PIPELINE_NAME = "dataengg"
# new content file 
dataDic = {
    f"invh_sdlf_{ENV}_{PIPELINE_NAME}_curated_db": {
        "LFTagKey": "module",
        "LFTagValues": ['transformed']
    },
    f"invh_sdlf_{ENV}_{PIPELINE_NAME}_transformed_db": {
        "LFTagKey": "module",
        "LFTagValues": ['curated']
    }
}
# new content file 
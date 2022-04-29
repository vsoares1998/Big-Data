
def create_dataset(project_id, display_name):
    """Create a dataset."""
   
    from google.cloud import automl

   
    project_id = "bdcc-project-201603999"
    display_name = "dataset_bdcc"

    client = automl.AutoMlClient()

    
    project_location = f"projects/{project_id}/locations/us-central1"

    metadata = automl.ImageClassificationDatasetMetadata(
        classification_type=automl.ClassificationType.MULTILABEL
    )
    dataset = automl.Dataset(
        display_name=display_name,
        image_classification_dataset_metadata=metadata,
    )

    # Create a dataset with the dataset metadata in the region.
    response = client.create_dataset(parent=project_location, dataset=dataset, timeout=300)

    created_dataset = response.result()

    # Display the dataset information
    print("Dataset name: {}".format(created_dataset.name))
    print("Dataset id: {}".format(created_dataset.name.split("/")[-1]))
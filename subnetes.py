from google.cloud import compute_v1
#from google.cloud.compute_v1.types import instance

def get_subnet_info(project_id, zone, subnet_name):
    """Get information about a subnet."""
    # [START compute_subnetworks_get_info]
    # project_id = 'your-project-id'
    # zone = 'us-central1-a'
    # subnet_name = 'your-subnet-name'
    client = compute_v1.SubnetworksClient()
    request = compute_v1.GetSubnetworkRequest(
        project=project_id,
        region=zone,
        subnetwork=subnet_name,
    )
    response = client.get(request=request)
    print(response)
    # [END compute_subnetworks_get_info]





 
    
import subprocess

def run_kubectl_command(command):
    try:
        result = subprocess.run(['kubectl'] + command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(e.stderr)  # Print error output for more details
        return None

def get_all_service_cluster_ips():
    return run_kubectl_command("get svc --output=jsonpath='{.items[*].spec.clusterIP}'")

def main():
    all_service_cluster_ips = get_all_service_cluster_ips()
    if all_service_cluster_ips:
        print("Cluster IPs of all services:")
        print(all_service_cluster_ips)

if __name__ == "__main__":
    main()

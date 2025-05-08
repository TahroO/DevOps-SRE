
provider "github" {
  token = trimspace(file(".gitHubToken"))
}
# Containers of Lambda
Container image support for AWS Lambda was announced back at AWS re:Invent 2020. This was a major new addition to the AWS functions-as-a-servjce offering. Lambda provides many benefits to developers in managing scaling, high availability and fault tolerance and enabliing a pay-per-value model. By supporting container packaginf for functions, Lmabda is now an option for a broader audience of developers

## Why did AWS add support for container packaging
Before this change, the lambda deployment package was a zip file which contained the libraries and dependencies. However, many customers have existing investments in container-based deployment tools and workflows. These include docker in addition to CICD, security and governance tools. With this change, developers can benefit from a uniform development and deployment

## Ways of Building a container image for a lambda Function
1. Using an AWS base image for lambda

The AWS base images are preloaded with a language runtime, a runtime interface client to manage the interaction between Lambda and your function code, and a runtime interface emulator for local testing.

2. Using an AWS OS-only base image

[AWS OS-only base images](https://gallery.ecr.aws/lambda/provided) contain an Amazon Linux distribution and the runtime interface emulator. These images are commonly used to create container images for compiled languages, such as Go and Rust, and for a language or language version that Lambda doesn't provide a base image for, such as Node.js 19. You can also use OS-only base images to implement a custom runtime. To make the image compatible with Lambda, you must include a runtime interface client for your language in the image.

3. Using a non-AWS base image

You can also use an alternative base image from another container registry, such as Alpine Linux or Debian. You can also use a custom image created by your organization. To make the image compatible with Lambda, you must include a runtime interface client for your language in the image.


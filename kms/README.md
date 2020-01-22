# AWS Key Management Service

AWS Key Management Service (KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data, and uses Hardware Security Modules (HSMs) to protect the security of your keys. AWS Key Management Service is integrated with several other AWS services to help you protect the data you store with these services.

Key Administrators are users or roles that will manage access to the encryption key.
Key Users are the users or roles that will use the key to encrypt and decrypt data.

# How
Amazon S3 and AWS KMS perform the following actions when you request that your data be decrypted.

* Amazon S3 sends the encrypted data key to AWS KMS
* AWS KMS decrypts the key by using the appropriate master key and sends the plaintext key back to Amazon S3
* Amazon S3 decrypts the ciphertext and removes the plaintext data key from memory as soon as possible

# Amazon CloudFront

Amazon CloudFront is a web service that accelerates the delivery of your content to your users through Amazon CloudFront's global network of edge locations.

Every resources you put to s3, it will delivery to CloudFront??
If full website was hosted in s3 (image, html files, ...), we can fully host the site using Amazon CloudFront.

`d30439rem8wzqr.cloudfront.net/cf1_lab.html`

Cache problem:
We can use invalidation setting to config our distribution to cache/ force expires an object. If you have a file that is updated frequently, you can still use Amazon CloudFront to cache it, but you can customize your cache expiration time. You can also choose not to cache a file, and Amazon CloudFront will accelerate content distribution using persistent connections and optimized routing from the origin.

If you want to nice URL for object, `http://www.example.com/images/image.jpg`
instead of `http://d111111abcdef8.cloudfront.net/images/image.jpg`, you should
create CNAME for `www.example.com`

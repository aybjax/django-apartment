def uploadTo(self, filename):
    path = self.getSellerPathForImage()
    filepath = 'apartment_images/%s/%s' % (
            path, filename
    )

    return filepath

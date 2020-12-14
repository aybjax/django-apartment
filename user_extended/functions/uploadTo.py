def uploadTo(self, filename):
    return "profile_image/%d_%s/%s" % (
            self.user.pk, self.user.username, filename
    )

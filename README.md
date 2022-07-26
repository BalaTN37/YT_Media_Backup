# YT_Media_Backup (Prototype)
Unlimited storage to backup Video and Photo automatically.
Batch of photos to be backuped are converted as a 4k video with timestamp of each photos recorded in SQLite DB
Batch of videos(including photos as video) to be backuped are uploaded using Google Cloud Project API.
Video will be stored in user's personal youtube account.
Uploaded Youtube video's URL is stored in DB.

For restoration of photos, video url and time stamp stored in DB used to retrieve.

App runs in background and monitors for any new photo/videos in device which needs to be backup

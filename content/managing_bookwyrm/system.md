---
Title: System Monitoring
Date: 2021-04-18
Order: 4
---

The `Admin > System` menu provides instance admins with a number of system monitoring features, and configuration options for background tasks.

## Imports

From the **Imports** page you can manage imports for books and both imports and exports for users. user exports are disabled by default. From this page you can monitor and, if necessary, cancel Book and User imports if they are causing errors, as well as setting limits on how often users can run imports. This is important if your instance is suffering performance problems due to a large number of import or export background jobs.

## Celery Status

The **Celery Status** page provides an overview of celery tasks and can provide an indication of which queues may be causing issues if your instance has become slow. From this page you can also clear entire queues and tasks, however this is generally a last resort as it may lead to data loss.

## Scheduled Tasks

You can monitor tasks schedules at `Admin > System > Scheduled Tasks`. Tasks are triggered from other pages.

## Email configuration

Check your outgoing email configuration here, and trigger a test email. This page may move in future.

## Connectors

Connectors are sources of data about books and authors. From this page you can enable or disable connectors, and set their priority. Other BookWyrm servers, Inventaire, and Open Library are enabled by default.

The priority determines the order in which search results appear. The highest priority is 1. The default priority is 2. Connector settings only determine whether a connector will be used to deliver search results. To handle federation and moderation, see `Admin > Federation` or `Admin > Moderation`.

## Files maintenance

This section is where you can configure a number of background jobs related to export and import files, and book cover images.

At **Schedule file deletion** you can schedule a regular job to delete user import and export files that have reached their expiry age. The expiry age is determined at **Export file expiration**.

The **Find book covers from connectors** section can help you with two different but related problems.

With **Find missing covers** you can set up a regular job to check for any books in your local database that do not have a cover image listed. This job searches Connectors for cover images they may be able to provide. This will, for example, enable you to pull in a cover image from a connected BookWyrm instance where it has recently been uploaded but there has not been any trigger for your instance to add the updated cover image. This can be resource intensive as it will run a search for every book in your database without a cover, so be cautious about how often you set this job to run.

The **Fix broken book cover filepaths** can be triggered, but not scheduled as a regular job. Most administrators will not need to run this job. This is designed to fix problems from server migrations where book records list a cover image, but the file does not exist in your file storage.
JOKE = "HaJiMiNanBeiLvDou"
SHORTER_JOKE = "dingdongji"
USER_ID = 123456
CURRENT_USER = {
    "data": {
        "id": str(USER_ID),
        "type": "user",
        "attributes": {
            "about": None,
            "age_verification_status": None,
            "apple_id": None,
            "can_see_nsfw": True,
            "created": "2024-01-01T01:00:00.000+00:00",
            "current_user_block_status": "none",
            "default_country_code": None,
            "discord_id": None,
            "email": f"{JOKE}@{SHORTER_JOKE}.com",
            "facebook": None,
            "facebook_id": None,
            "first_name": JOKE,
            "full_name": JOKE,
            "gender": 0,
            "google_id": None,
            "has_password": True,
            "image_url": JOKE,
            "is_deleted": False,
            "is_email_verified": True,
            "is_nuked": False,
            "is_suspended": False,
            "last_name": "",
            "social_connections": {
                "discord": None,
                "facebook": None,
                "google": None,
                "instagram": None,
                "reddit": None,
                "spotify": None,
                "spotify_open_access": None,
                "tiktok": None,
                "twitch": None,
                "twitter": None,
                "twitter2": None,
                "twitter_new_app": None,
                "vimeo": None,
                "youtube": None,
            },
            "thumb_url": JOKE,
            "twitch": None,
            "twitter": None,
            "url": f"https://www.patreon.com/user?u={USER_ID}",
            "vanity": None,
            "youtube": None,
        },
        "relationships": {
            "pledges": {
                "data": [
                    {
                        "id": str(USER_ID),
                        "type": "pledge",
                        "attributes": {
                            "amount_cents": 500,
                            "created_at": "2026-05-01T00:00:00.000+00:00",
                            "pledge_cap_cents": None,
                            "patron_pays_fees": False,
                        },
                        "relationships": {
                            "creator": {"data": {"id": "17223600", "type": "user"}},
                            "reward": {"data": {"id": "10053906", "type": "reward"}},
                        },
                    }
                ],
            },
        },
    },
    "links": {
        "self": f"https://www.patreon.com/api/user/{USER_ID}",
    },
}

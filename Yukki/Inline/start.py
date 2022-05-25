from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Səs keyfiyyəti", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Audio Səs", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Səlahiyyətli İstifadəçilər", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 İdarə paneli", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ ​​Bağlayın", callback_data="close"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Parametrlər**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Köməkçi Əmrləri Menyusu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Parametrlər", callback_data="settingm"
                )
            ],
        ]
        return f"🎛 **Budur {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Köməkçi Əmrləri Menyusu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Parametrlər", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Söhbət Qrupu", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛 **Budur {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Köməkçi Əmrləri Menyusu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Parametrlər", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Kanal", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛 **Budur {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Köməkçi Əmrləri Menyusu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Parametrlər", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Kanal", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨Support Qrupu", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛 **Budur {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Köməkçi Əmrləri Menyusu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Məni öz qrupuna əlavə et",
                    url=f"https://t.me/LuksMusicbot?startgroup=true",
                )
            ],
        ]
        return f"🎛 **Budur {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Köməkçi Əmrləri Menyusu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Məni öz qrupuna əlavə et",
                    url=f"https://t.me/LuksMusicbot?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Support Qrupu", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛 **Budur {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Köməkçi Əmrləri Menyusu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Məni öz qrupuna əlavə et",
                    url=f"https://t.me/LuksMusicbot?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Kanal", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛 **Budur {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Köməkçi Əmrləri Menyusu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Məni öz qrupuna əlavə et",
                    url=f"https://t.me/LuksMusicbot?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Kanal", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨Support Qrupu", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛 **Budur {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Audio Keyfiyyət", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Audio Həcmi", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Səlahiyyətli İstifadəçilər", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 İdarə paneli", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ ​​Bağlayın", callback_data="close"),
            InlineKeyboardButton(text="🔙 Geri qayıt", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Parametrlər**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Audio Səs səviyyəsini sıfırla 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 Aşağı Səs", callback_data="LV"),
            InlineKeyboardButton(text="🔉 Orta Səs", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 Yüksək Səs", callback_data="HV"),
            InlineKeyboardButton(text="🔈 Gücləndirilmiş Cild", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 Fərdi Həcm 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 Geri qayıt", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Parametrlər**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼Fərdi Həcm 🔼", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Parametrlər**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Hər kəs", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 Adminlər", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 Səlahiyyətli İstifadəçi Siyahıları", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 Geri qayıt", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Parametrlər**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ İş vaxtı", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 Geri qayıt", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Parametrlər**", buttons

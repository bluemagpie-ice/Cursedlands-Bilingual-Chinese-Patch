# ============================================================
# CursedLands 中文本地化（双语字幕）
# 本文件为汉化补丁：默认启用中文，并把对白/选项字体切换为
# 打包的 Noto Sans CJK（原默认 DejaVuSans 无中文字形，会显示乱码）。
# ============================================================

init python:
    # 默认语言设为中文（用户仍可在设置里切回英文）
    config.language = "chinese"

init 1000 python:

    import renpy.style as _style

    _regular = "fonts/NotoSansCJKsc-Regular.otf"
    _bold = "fonts/NotoSansCJKsc-Bold.otf"

    # 对白、角色名、菜单选项的字体（覆盖不含中文的默认字体）
    for _nm in ("say_dialogue", "say_label", "say_thought",
                "choice_button", "choice_button_text",
                "menu_choice", "menu_choice_button"):
        try:
            _s = _style.get_or_create_style(_nm)
            _s.font = _bold if _nm == "say_label" else _regular
        except Exception:
            pass

    # 缩小对白字号，容纳“英文\n中文”双语长文本
    try:
        _sd = _style.get_or_create_style("say_dialogue")
        _base = _sd.size
        if _base is None:
            _base = 22
        _sd.size = max(16, int(_base * 0.72))
        _sd.line_spacing = 0
    except Exception:
        pass

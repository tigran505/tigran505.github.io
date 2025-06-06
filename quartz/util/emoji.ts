const U200D = String.fromCharCode(8205)
const UFE0Fg = /\uFE0F/g

export function getIconCode(char: string) {
  return toCodePoint(char.indexOf(U200D) < 0 ? char.replace(UFE0Fg, "") : char)
}

function toCodePoint(unicodeSurrogates: string) {
  const r = []
  let c = 0,
    p = 0,
    i = 0

  while (i < unicodeSurrogates.length) {
    c = unicodeSurrogates.charCodeAt(i++)
    if (p) {
      r.push((65536 + ((p - 55296) << 10) + (c - 56320)).toString(16))
      p = 0
    } else if (55296 <= c && c <= 56319) {
      p = c
    } else {
      r.push(c.toString(16))
    }
  }
  return r.join("-")
}

type EmojiMap = {
  codePointToName: Record<string, string>
  nameToBase64: Record<string, string>
}

let emojimap: EmojiMap | undefined = undefined

// Добавляем поддержку некоторых флагов (составные codepoint)
const customFlagMap: Record<string, string> = {
  "1f1fa-1f1f8": "flag-us", // 🇺🇸
  "1f1f7-1f1fa": "flag-ru", // 🇷🇺
  // сюда можно добавить другие флаги по необходимости
}

// Функция загрузки emoji с поддержкой составных codepoint (например, флаги)
export async function loadEmoji(code: string) {
  if (!emojimap) {
    const data = await import("./emojimap.json")
    emojimap = data
  }

  // Сначала проверяем в нашем кастомном мапе (для флагов)
  if (customFlagMap[code.toLowerCase()]) {
    const name = customFlagMap[code.toLowerCase()]
    const b64 = emojimap.nameToBase64[name]
    if (!b64) throw new Error(`name ${name} not found in map`)
    return b64
  }

  // Стандартный поиск по одиночному codepoint
  const name = emojimap.codePointToName[`U+${code.toUpperCase()}`]
  if (!name) throw new Error(`codepoint ${code} not found in map`)

  const b64 = emojimap.nameToBase64[name]
  if (!b64) throw new Error(`name ${name} not found in map`)

  return b64
}

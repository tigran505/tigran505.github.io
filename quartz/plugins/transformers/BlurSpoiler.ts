import { QuartzTransformerPlugin } from "../types"
// @ts-ignore
import script from "../../components/scripts/_spoiler.inline.ts";
 
export const BlurText: QuartzTransformerPlugin = () => {
    const sym = "🤫"
    return {
      name: "BlurText",
      textTransform(_ctx, src) {
        src = String(src)
        const regex = new RegExp(`${sym}${sym}([^${sym}]+)${sym}${sym}`, "g")
        src = src.replace(regex, (value, ...[capture]) => {
            return `<span class="spoiler-text">${capture}</span>`
        })
        return src
    },
      externalResources() {
        return {
            js: [
                {
                    loadTime: "afterDOMReady",
                    moduleType: "module",
                    contentType: "inline",
                    script: script,
                },
            ]
        }
      },
    }
  }

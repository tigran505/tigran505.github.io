import { QuartzComponent, QuartzComponentConstructor } from "./types"

export default (() => {
  const Comments: QuartzComponent = ({ fileData }) => {
    const disableComment: boolean =
      typeof fileData.frontmatter?.comments !== "undefined" &&
      (!fileData.frontmatter?.comments || fileData.frontmatter?.comments === "false")

    if (disableComment) return <></>

    return (
      <script
        async
        src="https://comments.app/js/widget.js?3"
        data-comments-app-website="WM8-A9NO"
        data-limit="5"
        data-color="2A6EF5"
        data-dislikes="1"
        data-colorful="1"
      />
    )
  }

  return Comments
}) satisfies QuartzComponentConstructor
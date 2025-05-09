{displayClass && (
    <>
      {!displayClass.includes('mobile-only') && (
        <li>
          <a id="random-page-button-mobile" href="#">
            Random Page 🎲
          </a>
        </li>
      )}
      {!displayClass.includes('desktop-only') && (
        <li>
          <a id="random-page-button-desktop" href="#">
            Random Page 🎲
          </a>
        </li>
      )}
    </>
  )}
import Document, { Html, Head, Main, NextScript } from 'next/document';
import { ServerStyleSheet } from 'styled-components';

export default class MyDocument extends Document {
  static async getInitialProps(ctx) {
    const sheet = new ServerStyleSheet();
    const originalRenderPage = ctx.renderPage;

    try {
      ctx.renderPage = () =>
        originalRenderPage({
          enhanceApp: (App) => (props) =>
            sheet.collectStyles(<App {...props} />),
        });

      const initialProps = await Document.getInitialProps(ctx);
      return {
        ...initialProps,
        styles: [
          <>
            {initialProps.styles}
            {sheet.getStyleElement()}
          </>,
        ],
      };
    } finally {
      sheet.seal();
    }
  }

  render() {
    return (
      <Html>
        <Head>
          <meta charset="utf-8" />
          <meta name="apple-mobile-web-app-capable" content="yes"></meta>
          <meta
            property="og:title"
            content="clay – A native code editor for macOS"
          ></meta>
          <meta
            property="og:image"
            content="https://www.clay-code.vercel.app/social-preview.jpg"
          ></meta>
          <meta
            property="og:description"
            content="A lightweight, natively built editor. Open source. Free forever."
          ></meta>
          <meta property="og:url" content="https://www.clay-code.vercel.app"></meta>
          <meta
            name="twitter:image"
            content="https://www.clay-code.vercel.app/social-preview.jpg"
          ></meta>
          <meta
            name="twitter:image:src"
            content="https://www.clay-code.vercel.app/social-preview.jpg"
          ></meta>
          <meta name="twitter:card" content="summary_large_image"></meta>
          <meta name="twitter:site" content="@AsynchronousAI"></meta>
          <meta name="twitter:creator" content="@AsynchronousAI"></meta>
          <meta name="twitter:title" content="clay for macOS"></meta>
          <meta
            name="twitter:description"
            content="clay, a lightweight, natively built editor for macOS. Open source. Free forever."
          ></meta>
          <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}


import Image from 'next/image';
import styled from 'styled-components';
import { Parallax } from 'react-parallax';
import Typography from '@/components/common/Typography';
import { Row, Column, Section, Stack } from '@/components/common/layout';
import HeroImage from '../HeroImage';
import Button from '../../../common/Button';

const ProductIconWrap = styled.div`
  width: 128px;
  margin-left: auto;
  margin-right: auto;
`;

const HeroSection = () => {
  return (
    <Parallax
      style={{ overflow: 'visible' }}
      renderLayer={(percentage) => {
        return (
          <Section contained gutterTop>
            <Row align="center" style={{ position: 'relative', zIndex: 1 }}>
              <Column width={{ md: 12, lg: 12 }}>
                <Stack gap={2} align="center">
                  <ProductIconWrap>
                    <Image
                      width={128}
                      height={128}
                      src="/product-icon.png"
                      alt="clay product icon"
                    />
                  </ProductIconWrap>
                  <Typography variant="eyebrow-elevated" as="h1">
                    clay for macOS
                  </Typography>
                  <Typography variant="headline-elevated">
                    A modern runtime for all of your code.
                    Open source. Free forever.
                  </Typography>
                  <Typography variant="intro-elevated" color="tertiary" gutterBottom>
                    Clay is an exciting new runtime made for all your code to work in unity. Develop any project using any language at speeds like never before with increased efficienc and reliability, while being able to bind all your programming languages together as one, all while being open source and free forever.
                  </Typography>
                  <Button disabled>Download Coming Soon</Button>
                  <Typography variant="body-reduced" color="tertiary">v0.0.1 | macOS 12+ | Windows 10+ | Linux</Typography>
                </Stack>
              </Column>
            </Row>
            <Row align="center">
              <Column>
                <HeroImage percentage={percentage} />
              </Column>
            </Row>
          </Section>
        )
      }}
    />
  );
}

export default HeroSection;

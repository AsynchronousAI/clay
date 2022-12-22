import { useMemo } from 'react';
import { Feather, GitHub, Info, Layout, Sliders, Tool, Zap } from 'react-feather';
import Tile from '@/components/common/Tile';
import Typography from '@/components/common/Typography';
import { Grid, GridItem, Section, Stack } from '@/components/common/layout';
import { useSite } from '@/components/common/Site';

const IntroFeaturesSection = () => {
  const { breakpoint } = useSite();

  const gap = useMemo(() => breakpoint === 'xs' ? 24 : 40, [breakpoint])
  
  return (
    <Section contained gutterBottom={20} variant="secondary">
      <Grid columns={{ xs: 1, lg: 2 }} gap={{ xs: 6, lg: 12 }}>
        <GridItem as={Tile} width={{ xs: 1, lg: 2 }}>
          <Stack direction={breakpoint === 'xs' ? "vertical" : "horizontal"} gap={3.5} >
            <div>
              <Info size={28} /> 
            </div>
            <Typography variant="intro">
              Clay is meant to be a runtime where your code runs incredibly fast and efficiently while being able to bind all your programming languages together as one.
            </Typography>
          </Stack>
        </GridItem>
        <GridItem>
          <Stack>
            <Zap size={gap} />
            <Typography variant="intro" gutterTop>Incredible Speeds</Typography>
            <Typography variant="intro" style={{ opacity: .5 }}>
              Experience your code running faster with a brand new upgraded compiler for every language you use.
            </Typography>
          </Stack>
        </GridItem>
        <GridItem>
          <Stack>
            <Feather size={gap} />
            <Typography variant="intro" gutterTop>
              Lightweight
            </Typography>
            <Typography variant="intro" style={{ opacity: .5 }}>
              Designed to be simple with a limitless potential, clay is the perfect runtime for any project.
            </Typography>
          </Stack>
        </GridItem>
        <GridItem>
          <Stack>
            <GitHub size={gap} />
            <Typography variant="intro" gutterTop>
              Completely Open Source
            </Typography>
            <Typography variant="intro" style={{ opacity: .5 }}>
              Clay is developed for you by developers like you. Don&apos;t like something? Want a new feature? Just create an issue or submit a PR.
            </Typography>
          </Stack>
        </GridItem>
        <GridItem>
          <Stack>
            <Sliders size={gap} />
            <Typography variant="intro" gutterTop>
              Unified Languages
            </Typography>
            <Typography variant="intro" style={{ opacity: .5 }}>
              Clay allows you to bind all your languages together. No more picking which language is best, Why not use them all at once?
            </Typography>
          </Stack>
        </GridItem>
        <GridItem>
          <Stack>
            <Layout size={gap} />
            <Typography variant="intro" gutterTop>
              Globalized Packages
            </Typography>
            <Typography variant="intro" style={{ opacity: .5 }}>
              All of your favorite packages no longer need to be used in a single language. Why limit yourself? Use any package in any language.
            </Typography>
          </Stack>
        </GridItem>
        <GridItem>
          <Stack>
            <Tool size={gap} />
            <Typography variant="intro" gutterTop>
              Utility Belts
            </Typography>
            <Typography variant="intro" style={{ opacity: .5 }}>
              Install utility belts which gives you a set of tools to use in your code. Making a website? Install the web utilities and get all the tools you need.
            </Typography>
          </Stack>
        </GridItem>
      </Grid>
    </Section>
  );
}

export default IntroFeaturesSection;

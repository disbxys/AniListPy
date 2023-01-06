
EPISODE_NUMS = '''
query ($id: Int) {
    Media(id: $id, type: ANIME) {
        streamingEpisodes {
            title
            url
            thumbnail
            site
        }
    }
}
'''

USERDATA = '''
query ($username: String, $type: MediaType) {
    MediaListCollection(userName: $username, type: $type) {
        user {
            id
            name
            siteUrl
            avatar {
                large
            }
        }
        lists {
            name
            status
            entries {
                id
                status
                progress
                media {
                    id
                    idMal
                    title {
                        english
                        romaji
                        userPreferred
                    }
                    status
                    genres
                }
                score(format: POINT_10)
                notes
                repeat
            }
        }
    }
}
'''

ANIME_ID = '''
query ($id: Int) {
    Media(id: $id, type: ANIME) {
        siteUrl
        id
        idMal
        title {
            english
            romaji
        }
        coverImage {
            extraLarge
        }
        bannerImage
        description
        favourites
        popularity
        genres
        type
        format
        episodes
        season
        seasonYear
        status
        averageScore
        streamingEpisodes {
            title
            thumbnail
            url
            site
        }
        airingSchedule {
            edges {
                id
                node {
                    media {
                        id
                    }
                    episode
                    airingAt
                }
            }
        }
        trailer {
            id
        }
        studios {
            nodes {
                name
            }
        }
        tags {
            name
        }
        characters {
            nodes {
                image {
                    large
                }
                siteUrl
            }
        }
        relations {
            nodes {
                coverImage {
                    extraLarge
                }
                siteUrl
            }
        }
        trailer {
            id
            site
            thumbnail
        }
        recommendations {
            nodes {
                mediaRecommendation {
                    siteUrl
                    coverImage {
                        extraLarge
                    }
                }
            }
        }
    }
}
'''

ANIME_IDMAL = '''
query ($idMal: Int) {
    Media(idMal: $idMal, type: ANIME) {
        siteUrl
        id
        idMal
        title {
            english
            romaji
        }
        coverImage {
            extraLarge
        }
        bannerImage
        description
        favourites
        popularity
        genres
        type
        format
        episodes
        season
        seasonYear
        status
        averageScore
        streamingEpisodes {
            title
            thumbnail
            url
            site
        }
        airingSchedule {
            edges {
                id
                node {
                    media {
                        id
                    }
                    episode
                    airingAt
                }
            }
        }
        trailer {
            id
        }
        studios {
            nodes {
                name
            }
        }
        tags {
            name
        }
        characters {
            nodes {
                image {
                    large
                }
                siteUrl
            }
        }
        relations {
            nodes {
                coverImage {
                    extraLarge
                }
                siteUrl
            }
        }
        trailer {
            id
            site
            thumbnail
        }
        recommendations {
            nodes {
                mediaRecommendation {
                    siteUrl
                    coverImage {
                        extraLarge
                    }
                }
            }
        }
    }
}
'''

ANIME_SEARCH = '''
query ($search: String) {
    Media(search: $search, type: ANIME) {
        siteUrl
        id
        idMal
        title {
            english
            romaji
        }
        coverImage {
            extraLarge
        }
        bannerImage
        description
        favourites
        popularity
        genres
        type
        format
        episodes
        season
        seasonYear
        status
        averageScore
        streamingEpisodes {
            title
            thumbnail
            url
            site
        }
        airingSchedule {
            edges {
                id
                node {
                    media {
                        id
                    }
                    episode
                    airingAt
                }
            }
        }
        studios {
            nodes {
                name
            }
        }
        tags {
            name
        }
        characters {
            nodes {
                image {
                    large
                }
                siteUrl
            }
        }
        relations {
            nodes {
                coverImage {
                    extraLarge
                }
                siteUrl
            }
        }
        trailer {
            id
            site
            thumbnail
        }
        recommendations {
            nodes {
                mediaRecommendation {
                    siteUrl
                    coverImage {
                        extraLarge
                    }
                }
            }
        }
    }
}
'''

MANGA_ID = '''
query ($id: Int) {
    Media (id: $id, type: MANGA) {
        siteUrl
        id
        idMal
        title {
            english
            romaji
            native
            userPreferred
        }
        coverImage {
            extraLarge
        }
        startDate {
            year
            month
            day
        }
        bannerImage
        isAdult
        description
        favourites
        popularity
        genres
        type
        format
        chapters
        volumes
        airingSchedule {
            edges {
                id
                node {
                    media {
                        id
                    }
                    episode
                    airingAt
                }
            }
        }
        status
        averageScore
        tags {
            id
            name
            isAdult
            isMediaSpoiler
            isGeneralSpoiler
        }
        trailer {
            id
            thumbnail
            site
        }
        characters {
            nodes {
                name {
                    first
                    middle
                    last
                    full
                    native
                    userPreferred
                }
                gender
                age
                dateOfBirth {
                    year
                    month
                    day
                }
                image {
                    large
                }
                siteUrl
            }
        }
        staff {
            edges {
                id
                node {
                    name {
                        first
                        middle
                        last
                        full
                        native
                        userPreferred
                    }
                    dateOfBirth {
                        year
                        month
                        day
                    }
                    gender
                    description
                    bloodType
                    yearsActive
                    modNotes
                    homeTown
                }
            }
        }
        isLicensed
        relations {
            nodes {
                coverImage {
                    extraLarge
                }
                siteUrl
            }
        }
        trailer {
            id
            site
            thumbnail
        }
        recommendations {
            nodes {
                mediaRecommendation {
                    siteUrl
                    coverImage {
                        extraLarge
                    }
                }
            }
        }
    }
}
'''

MANGA_IDMAL = '''
query ($idMal: Int) {
    Media (idMal: $idMal, type: MANGA) {
        siteUrl
        id
        idMal
        title {
            english
            romaji
            native
            userPreferred
        }
        coverImage {
            extraLarge
        }
        startDate {
            year
            month
            day
        }
        bannerImage
        isAdult
        description
        favourites
        popularity
        genres
        type
        format
        chapters
        volumes
        airingSchedule {
            edges {
                id
                node {
                    media {
                        id
                    }
                    episode
                    airingAt
                }
            }
        }
        status
        averageScore
        tags {
            id
            name
            isAdult
            isMediaSpoiler
            isGeneralSpoiler
        }
        trailer {
            id
            thumbnail
            site
        }
        characters {
            nodes {
                name {
                    first
                    middle
                    last
                    full
                    native
                    userPreferred
                }
                gender
                age
                dateOfBirth {
                    year
                    month
                    day
                }
                image {
                    large
                }
                siteUrl
            }
        }
        staff {
            edges {
                id
                node {
                    name {
                        first
                        middle
                        last
                        full
                        native
                        userPreferred
                    }
                    dateOfBirth {
                        year
                        month
                        day
                    }
                    gender
                    description
                    bloodType
                    yearsActive
                    modNotes
                    homeTown
                }
            }
        }
        isLicensed
        relations {
            nodes {
                coverImage {
                    extraLarge
                }
                siteUrl
            }
        }
        trailer {
            id
            site
            thumbnail
        }
        recommendations {
            nodes {
                mediaRecommendation {
                    siteUrl
                    coverImage {
                        extraLarge
                    }
                }
            }
        }
    }
}
'''

MANGA_SEARCH = '''
query ($search: String) {
    Media (search: $search, type: MANGA) {
        siteUrl
        id
        idMal
        title {
            english
            romaji
            native
            userPreferred
        }
        coverImage {
            extraLarge
        }
        startDate {
            year
            month
            day
        }
        bannerImage
        isAdult
        description
        favourites
        popularity
        genres
        type
        format
        chapters
        volumes
        airingSchedule {
            edges {
                id
                node {
                    media {
                        id
                    }
                    episode
                    airingAt
                }
            }
        }
        status
        averageScore
        tags {
            id
            name
            isAdult
            isMediaSpoiler
            isGeneralSpoiler
        }
        trailer {
            id
            thumbnail
            site
        }
        characters {
            nodes {
                name {
                    first
                    middle
                    last
                    full
                    native
                    userPreferred
                }
                gender
                age
                dateOfBirth {
                    year
                    month
                    day
                }
                image {
                    large
                }
                siteUrl
            }
        }
        staff {
            edges {
                id
                node {
                    name {
                        first
                        middle
                        last
                        full
                        native
                        userPreferred
                    }
                    dateOfBirth {
                        year
                        month
                        day
                    }
                    gender
                    description
                    bloodType
                    yearsActive
                    modNotes
                    homeTown
                }
            }
        }
        isLicensed
        relations {
            nodes {
                coverImage {
                    extraLarge
                }
                siteUrl
            }
        }
        trailer {
            id
            site
            thumbnail
        }
        recommendations {
            nodes {
                mediaRecommendation {
                    siteUrl
                    coverImage {
                        extraLarge
                    }
                }
            }
        }
    }
}
'''

MEDIA_PAGE_LIST = '''
query ($page: Int, $perPage: Int, $type: MediaType) {
    Page(page: $page, perPage: $perPage) {
        pageInfo {
            total
            perPage
            currentPage
            lastPage
            hasNextPage
        }
        media(type: $type) {
            siteUrl
            id
            idMal
            title {
                english
                romaji
                native
                userPreferred
            }
            synonyms
            coverImage {
                extraLarge
                large
            }
            bannerImage
            status(version: 2)
            startDate {
                year
                month
                day
            }
            endDate {
                year
                month
                day
            }
            type
            format
            episodes
            duration
            chapters
            volumes
            season
            seasonYear
            description
            isAdult
            isLocked
            isLicensed
            genres
            source(version: 3)
            favourites
            isFavourite
            isRecommendationBlocked
            isFavouriteBlocked
            isReviewBlocked
            popularity
            meanScore
            averageScore
            tags {
                id
                name
                description
                rank
                isAdult
                isMediaSpoiler
                isGeneralSpoiler
                userId
            }
            hashtag
            countryOfOrigin
            trailer {
                id
                thumbnail
                site
            }
            nextAiringEpisode {
                id
                airingAt
                timeUntilAiring
                episode
            }
            characters {
                nodes {
                    name {
                        first
                        middle
                        last
                        full
                        native
                        userPreferred
                    }
                    gender
                    age
                    dateOfBirth {
                        year
                        month
                        day
                    }
                    image {
                        large
                    }
                    siteUrl
                }
            }
            staff {
                edges {
                    id
                    node {
                        name {
                            first
                            middle
                            last
                            full
                            native
                            userPreferred
                        }
                        dateOfBirth {
                            year
                            month
                            day
                        }
                        gender
                        description
                        bloodType
                        yearsActive
                        modNotes
                        homeTown
                    }
                }
            }
            relations {
                edges {
                    id
                    relationType(version: 2)
                    node {
                        id
                        idMal
                        title {
                            english
                            romaji
                            native
                            userPreferred
                        }
                        format
                        type
                        status(version: 2)
                        coverImage {
                            extraLarge
                            large
                        }
                        bannerImage
                        siteUrl
                    }
                }
            }
            characterPreview: characters(sort: [ROLE, RELEVANCE, ID]) {
                edges {
                    id
                    role
                    name
                    voiceActors(language: JAPANESE, sort: [RELEVANCE, ID]) {
                        id
                        name {
                            full
                            native
                            alternative
                            userPreferred
                        }
                        language: languageV2
                        image {
                            large
                        }
                    }
                    node {
                        id
                        name {
                            full
                            native
                            alternative
                            alternativeSpoiler
                            userPreferred
                        }
                        image {
                            large
                        }
                    }
                }
            }
            staffPreview: staff(sort: [RELEVANCE, ID]) {
                edges {
                    id
                    role
                    node {
                        id
                        name {
                            full
                            native
                            alternative
                            userPreferred
                        }
                        age
                        gender
                        homeTown
                        dateOfBirth {
                            year
                            month
                            day
                        }
                        yearsActive
                        language: languageV2
                        image {
                            large
                        }
                        primaryOccupations
                        isFavourite
                        isFavouriteBlocked
                    }
                }
            }
            studios {
                edges {
                    isMain
                    node {
                        id
                        name
                        siteUrl
                        isFavourite
                        isAnimationStudio
                    }
                }
            }
            rankings {
                id
                rank
                format
                year
                season
                allTime
                context
            }
            recommendations(sort: [RATING_DESC, ID]) {
                nodes {
                    id
                    rating
                    userRating
                    mediaRecommendation {
                        siteUrl
                        id
                        idMal
                        title {
                            english
                            romaji
                            native
                            userPreferred
                        }
                        format
                        type
                        status(version: 2)
                        coverImage {
                            extraLarge
                            large
                        }
                        bannerImage
                    }
                    user {
                        id
                        name
                        avatar {
                            large
                        }
                    }
                }
            }
            externalLinks {
                id
                site
                url
                type
                language
                color
                icon
                notes
                isDisabled
            }
            stats {
                statusDistribution {
                    status
                    amount
                }
                scoreDistribution {
                    score
                    amount
                }
            }
        }
    }
}

'''
